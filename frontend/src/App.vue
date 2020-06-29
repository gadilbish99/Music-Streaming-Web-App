<template>
  <v-app>
    <div v-if="isLoggedIn">
      <NavigationDrawer/>
      <Toolbar/>
      <Player/>
    </div>
    <router-view></router-view>
  </v-app>
</template>

<script>
import NavigationDrawer from "@/components/NavigationDrawer.vue";
import Player from "@/components/Player.vue";
import Toolbar from "@/components/Toolbar.vue";

export default {
  name: 'App',
  components: {
    NavigationDrawer, 
    Player,
    Toolbar
  },
  computed : {
    isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
  },
}
</script>