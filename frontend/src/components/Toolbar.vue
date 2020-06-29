<template>
    <v-toolbar
        :color="color"
        fixed
        clipped-left
        app
    >
        <v-icon class="mx-3">library_music</v-icon>
        <v-toolbar-title class="mr-5 align-center">
          <span class="title">Music Streaming App</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
        v-model="query"
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="search"
        label="Search"
        dark
        @click="showResult"
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-btn text @click="logout">Log Out</v-btn>
    </v-toolbar>
</template>

<script>

export default {
  components: {
    
  },
  data () {
    return {
      query: "",
      color: "green"
    }
  },
  watch: {
    query: function (val) {
      if (val.length > 0) {
        this.$store.dispatch("search", {"query": val})
        .then(()=>{            
          this.$router.push('/search')
        })
      }
      else {
        this.$store.dispatch("resetSearchResults")
        this.$router.push('/')
      }
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      .then(()=>{            
        this.$router.push('/login')
      })
    },
    showResult() {
      this.$router.push('/search')
    }
  }
}
</script>
