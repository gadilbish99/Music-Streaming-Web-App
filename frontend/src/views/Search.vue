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
      query: "",
      color: "green"
    }
  },
  computed: {
    feeds() {
      return this.$store.getters.feeds
    }
  }
}
</script>