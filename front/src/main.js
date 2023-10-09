import {createApp} from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import {components, directives} from "vuetify/dist/vuetify";
import {createVuetify} from "vuetify";


const vuetify = createVuetify({
    components,
    directives,
})

const app = createApp(App).use(router, axios)
app.use(store);
app.use(vuetify);
app.mount('#app')

