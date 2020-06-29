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
    this.$store.dispatch('getSongs')
    .then(result => {
      this.feeds = result
    })
  }
}
</script>