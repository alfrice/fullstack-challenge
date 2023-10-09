import {createRouter, createWebHistory} from "vue-router";
import RegisterView from "@/views/RegisterView.vue";
import LoginView from "@/views/LoginView.vue";
import PropertiesView from "@/views/PropertiesView.vue";
import LogoutView from "@/views/LogoutView.vue";


var items = [
    {
        path: "/login",
        name: "login",
        component: LoginView,
    },
    {
        path: "/logout",
        name: "logout",
        component: LogoutView,
    },
    {
        path: "/register",
        name: "register",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: RegisterView
    }, {
        path: "/properties",
        name: "properties",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: PropertiesView
    },
];
const routes = items

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
