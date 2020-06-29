<template>
    <v-flex xs6 sm4 md3 lg2 >
        <v-card class="ma-3">
            <v-img
                :src="img_url"
                @click="play"
            ></v-img>

            <v-card-title primary-title>
                <div>
                    <b> {{ truncate(song) }} </b>
                    <div> {{ truncate(artist) }} </div>
                </div>
            </v-card-title>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn icon @click="remove" v-if="isFavoriteSongs">
                    <v-icon color="green">favorite_border</v-icon>
                </v-btn>
                <v-btn icon @click="add" v-else>
                    <v-icon color="green">favorite</v-icon>
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-flex>
</template>

<script>
  export default {
    props: {
      feed: Object
    },
    methods: {
        truncate(str) {
            if (str.length > 15) {
                return str.slice(0, 12) + "..."
            }
            else
                return str
        },

        play() {
            this.$root.$emit('play', this.feed)
        },

        add() {
            this.$store.dispatch('addFavoriteSong', {"id" : this.feed.pk})
        },

        remove() {
            this.$store.dispatch('removeFavoriteSong', {"id" : this.feed.pk})
            .then(result => {
                if (result.message == 'Removed') {
                    this.$root.$emit('refreshFavoriteSongs')
                }
            })
        }
    },
    computed: {
        song() {
            return this.feed.song_title
        },
        artist() {
            return this.feed.artist_name
        },
        img_url() {
            return this.feed.img_url
        },
        song_url() {
            return this.feed.song_url
        },
        isFavoriteSongs() {
            return this.$route.path == '/favorite_songs'
        }
    }
  }
</script>
