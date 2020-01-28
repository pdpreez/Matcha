import Vue from 'vue'
import Router from 'vue-router'
import login from './pages/Login.vue'
import register from './pages/Register.vue'

Vue.use(Router)

const router = new Router({
    mode: "history",
    routes: [
        { path: "/", name:"home"},
        { path: "/login", component: login, name: "login"},
        { path: "/register", component: register, name:"register"},
    ]
})

export default router