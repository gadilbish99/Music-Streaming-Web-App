<template>
  <v-content>
    <v-container class="my-3">
        <v-layout row wrap>
          <Card v-for="feed in feeds" :key="feed.id" :feed="feed"/>
        </v-layout>
    </v-container>
  </v-content>
</template>

<script>
import Card from "./Card.vue"

export default {
  components: {
    Card
  },
  props: {
    feeds: Array
  }
}
</script>