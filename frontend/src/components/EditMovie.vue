<script setup>
import {reactive} from "vue";
import {useStore} from "vuex";
import {useRoute} from "vue-router";

const props = defineProps({
  actors: {
    type: Array,
    default: () => [],
  },
  actorsList: {
    type: Array,
    default: () => [],
  },
  description: String,
  callback: {
    type: Function,
    default: () => {},
  }
})

const route = useRoute();
const store = useStore();

const body = reactive({
  description: props.description,
  actors: [...props.actors],
})

const save = () => {
  store.dispatch('editMovie', {
    movieId: route.params.movieId,
    data: body,
  }).then(props.callback);
}
</script>

<template>
  <v-card-text>
    <v-form @submit.prevent>
      <v-textarea
          class="description"
          label="Description"
          v-model="body.description"
      />
      <v-select
        label="Actors"
        v-model="body.actors"
        :items="actorsList"
        :item-title="(({first_name, last_name}) => `${first_name} ${last_name}`)"
        item-value="id"
        multiple
      />
    </v-form>
  </v-card-text>
  <v-card-actions class="justify-center">
    <v-btn
      @click="save"
      variant="outlined"
    >
      Save
    </v-btn>
  </v-card-actions>
</template>

<style scoped>
.description {
  margin-bottom: 0.5rem;
}
</style>
