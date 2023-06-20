<script setup>
import {onMounted} from "vue";
import {useStore} from "vuex";

const store = useStore()

onMounted(() => {
  store.dispatch('getActors');
})
</script>

<template>
  <v-app>
    <v-container>
      <v-card class="pa-8">
        <router-view />
      </v-card>
    </v-container>
  </v-app>
</template>

<style scoped>
</style>
