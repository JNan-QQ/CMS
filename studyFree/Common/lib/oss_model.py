# -*- coding: utf-8 -*-

import os

import oss2


class ossApi:
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', '')
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', '')
    bucket_name = os.getenv('OSS_TEST_BUCKET', 'syud')
    endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-.aliyuncs.com')

    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

    def upload(self, oss_filePath, fileStr):
        self.bucket.put_object(oss_filePath, fileStr)

    def simple_upload(self, oss_filePath, filename):
        oss2.resumable_upload(self.bucket, oss_filePath, filename)

    def determine_part_upload(self, oss_filePath, filename):
        # 也可以直接调用分片上传接口。
        # 首先可以用帮助函数设定分片大小，设我们期望的分片大小为128KB
        total_size = os.path.getsize(filename)
        part_size = oss2.determine_part_size(total_size, preferred_size=128 * 1024)
        # 初始化分片上传，得到Upload ID。接下来的接口都要用到这个Upload ID。
        upload_id = self.bucket.init_multipart_upload(oss_filePath).upload_id

        # 逐个上传分片
        # 其中oss2.SizedFileAdapter()把fileobj转换为一个新的文件对象，新的文件对象可读的长度等于size_to_upload
        with open(filename, 'rb') as fileobj:
            parts = []
            part_number = 1
            offset = 0
            while offset < total_size:
                size_to_upload = min(part_size, total_size - offset)
                result = self.bucket.upload_part(oss_filePath, upload_id, part_number,
                                                 oss2.SizedFileAdapter(fileobj, size_to_upload))
                parts.append(oss2.models.PartInfo(part_number, result.etag, size=size_to_upload, part_crc=result.crc))

                offset += size_to_upload
                part_number += 1

            # 完成分片上传
            self.bucket.complete_multipart_upload(oss_filePath, upload_id, parts)

    def download(self, oss_filePath, filename):
        self.bucket.get_object_to_file(oss_filePath, filename)

    def simple_download(self, oss_filePath, filename):
        # 断点续传下载
        oss2.resumable_download(self.bucket, oss_filePath, filename,
                                multiget_threshold=200 * 1024,
                                part_size=100 * 1024,
                                num_threads=3)


if __name__ == '__main__':
    ossApi().determine_part_upload('123.txt', r'')
    ossApi().download('123.txt', r'')
