import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from "../views/MovieList.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HelloWorld,
    },
  ],
});

export default router;
