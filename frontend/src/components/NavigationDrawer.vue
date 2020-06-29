<template>
  <v-navigation-drawer
    class="green"
    dark
    clipped
    app
    permanent
  >
    <v-list>
      <v-list-tile
        v-for="item in items"
        :key="item.title"
        router :to="item.route"
      >
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>

        <v-list-tile-content>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  export default {
    name: 'NavigationDrawer',
    data () {
      return {
        items: [
          { title: 'Profile', icon: 'person', route: '/profile' },
          { title: 'Home', icon: 'home', route: '/' },
          { title: 'Search', icon: 'search', route: '/search' },
          { title: 'Favorite Songs', icon: 'favorite', route: '/favorite_songs' }
        ]
      }
    }
  }
</script>