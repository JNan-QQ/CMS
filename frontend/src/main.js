import {createApp, h} from 'vue'
import Admin from './pages/Admin.vue'
import Login from './pages/Login.vue'
import Home from './pages/Home.vue'
import NotFoundComponent from './pages/404.vue'

const routes = {
    '/': Home,
    '/login': Login,
    '/admin': Admin,
}

const SimpleRouterApp = {
    data: () => ({
        currentRoute: window.location.pathname
    }),

    computed: {
        CurrentComponent() {
            return routes[this.currentRoute] || NotFoundComponent
        }
    },

    render() {
        return h(this.CurrentComponent)
    }

}

createApp(SimpleRouterApp).mount('#app')
// createApp(App).mount('#app')

