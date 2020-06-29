<template>
  <CardLayout :feeds="feeds"/>
</template>

<script>
import CardLayout from "@/components/CardLayout.vue";

export default {
  components: {
    CardLayout
  },
  data () {
    return {
      feeds: [] 
    }
  },
  mounted() {
    this.fetch()
    this.$root.$on('refreshFavoriteSongs', () => {
        this.fetch()
    })
  },

  methods: {
    fetch() {
      this.$store.dispatch('getFavoriteSongs')
      .then(result => {
        this.feeds = result
      })
    }
  }
}
</script>