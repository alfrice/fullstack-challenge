import {createStore} from "vuex";
import axios from "axios";


axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';


const store = createStore({
    state: {
        isAuthenticated: false,
        token: '',
        realEstateListings: {}
    },
    getters: {
        isAuthenticated: (state) => state.isAuthenticated,
        token: (state) => state.token,
        getListings: (state) => state.realEstateListings
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }

        },
        setRealEstateListings(state, props) {
            state.realEstateListings = props;
        },
        setToken(state, token) {
            state.token = token;
            state.isAuthenticated = true

        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
            console.log('removeToken')

        }


    },

});
export default store;

