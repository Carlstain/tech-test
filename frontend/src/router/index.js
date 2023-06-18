import { createRouter, createWebHistory } from 'vue-router';
import MovieList from "../views/MovieList.vue";
import Movie from "../views/Movie.vue";
import Home from "../views/Home.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/movies',
      name: 'movies',
      component: MovieList,
      children: [
        {
          path: ':movieId',
          name: 'movie',
          component: Movie
        }
      ]
    },
  ],
});

export default router;
