import Vue from 'vue'
import VueRouter from 'vue-router'
import goTo from 'vuetify/es5/services/goto'
import Missing from '../views/404.vue'
import Demo from '../views/Demo.vue'
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
Vue.use(VueRouter)

const routes = [{
        path: '/',
        component: Demo,
        meta: {
            title: 'Rainfo || Creative Minimal Portfolio'
        }
    },
    {
        path: '/main-demo',
        name: 'MainDemo',
        meta: {
            title: 'Rainfo || Main Demo Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MainDemo.vue')
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },

    {
        path: '/freelancer',
        name: 'Freelancer',
        meta: {
            title: 'Rainfo || Freelancer Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/Freelancer.vue')
    },
    {
        path: '/agency',
        name: 'Agency',
        meta: {
            title: 'Rainfo || Agency Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/Agency.vue')
    },
    {
        path: '/minimal-agency',
        name: 'MinimalAgency',
        meta: {
            title: 'Rainfo || Minimal Agency Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MinimalAgency.vue')
    },
    {
        path: '/creative-portfolio',
        name: 'CreativePortfolio',
        meta: {
            title: 'Rainfo || Creative Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/CreativePortfolio.vue')
    },
    {
        path: '/designer-portfolio',
        name: 'DesignerPortfolio',
        meta: {
            title: 'Rainfo || Designer Portfolio'
        },

        component: () =>
            import ('../views/all-home-version/DesignerPortfolio.vue')
    },
    {
        path: '/vertical-portfolio',
        name: 'VerticalPortfolio',
        meta: {
            title: 'Rainfo || Vertical Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/VerticalPortfolio.vue')
    },
    {
        path: '/multiscroll-portfolio',
        name: 'MultiScrollPortfolio',
        meta: {
            title: 'Rainfo || Multiscroll Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/MultiScrollPortfolio.vue')
    },
    {
        path: '/parallax-home',
        name: 'ParallaxHome',
        meta: {
            title: 'Rainfo || Parallax Portfolio'
        },
        component: () =>
            import ('../views/all-home-version/ParallaxHome.vue')
    },
    {
        path: '/portfolio-details',
        name: 'PortfolioDetails',
        meta: {
            title: 'Rainfo || Portfolio Details'
        },
        component: () =>
            import ('../views/PortfolioDetails.vue')
    },
    {
        path: '/service-details',
        name: 'ServiceDetails',
        meta: {
            title: 'Rainfo || Service Details'
        },
        component: () =>
            import ('../views/ServiceDetails.vue')
    },
    {
        path: '/blog-details',
        name: 'BlogDetails',
        meta: {
            title: 'Rainfo || Blog Details'
        },
        component: () =>
            import ('../views/BlogDetails.vue')
    },
    {
        path: '/contact',
        name: 'Contact',
        meta: {
            title: 'Rainfo || Contact'
        },
        component: () =>
            import ('../views/Contact.vue')
    },
    {
        path: '/about-us',
        name: 'AboutUs',
        meta: {
            title: 'Rainfo || AboutUs'
        },
        component: () =>
            import ('../views/AboutUs.vue')
    },
    {
        path: '/awards',
        name: 'Awards',
        meta: {
            title: 'Rainfo || Awards'
        },
        component: () =>
            import ('../views/Awards.vue')
    },
    {
        path: '/blog',
        name: 'Blog',
        meta: {
            title: 'Rainfo || Blog'
        },
        component: () =>
            import ('../views/Blog.vue')
    },
    {
        path: '/portfolio',
        name: 'Portfolio',
        meta: {
            title: 'Rainfo || Portfolio'
        },
        component: () =>
            import ('../views/Portfolio.vue')
    },
    {
        path: '/service',
        name: 'Service',
        meta: {
            title: 'Rainfo || Service'
        },
        component: () =>
            import ('../views/Service.vue')
    },
    {
        path: '*',
        component: Missing,
        meta: {
            title: 'Rainfo || 404'
        },
    }
]

const router = new VueRouter({
    mode: 'history',
    routes,
    scrollBehavior: (to, from, savedPosition) => {
        let scrollTo = 0

        if (to.hash) {
            scrollTo = to.hash
        } else if (savedPosition) {
            scrollTo = savedPosition.y
        }

        return goTo(scrollTo)
    },
})

router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    next()
})


export default router