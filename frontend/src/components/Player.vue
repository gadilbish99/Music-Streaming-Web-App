<template>
    <v-footer 
        fixed 
        height="auto" 
        app
    >
        <v-layout>
            <v-flex>
                <v-card tile>
                    <v-list>
                        <v-layout row align-center justify-center>
                            <v-list-tile>
                                <v-list-tile-content>
                                    <v-list-tile-title>{{song_title}}</v-list-tile-title>
                                    <v-list-tile-sub-title>{{artist_name}}</v-list-tile-sub-title>
                                </v-list-tile-content>

                                <v-spacer></v-spacer>
                                <v-list-tile-action>
                                    <v-btn icon @click="pause" v-if="isPlaying">
                                        <v-icon large :color="color">pause_circle_outline</v-icon>
                                    </v-btn>
                                    <v-btn icon @click="play" v-else>
                                        <v-icon large :color="color">play_circle_outline</v-icon>
                                    </v-btn>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-layout>
                        <v-progress-linear
                            v-model="value"
                            :color="color"
                            class="my-2"
                            height="10"
                        ></v-progress-linear>
                    </v-list>
                </v-card>
            </v-flex>
        </v-layout>
    </v-footer>
</template>

<script>
import {Howl} from 'howler';

export default {
    data () {
        return {
            color: "green",
            isPlaying: false,
            audio: null,
            value: 0,

            song_url: '',
            song_title: '',
            artist_name: ''
        }
    },
    methods: {
        begin() {
            if (this.song_url) {
                fetch(this.song_url)
                .then(response => response.blob())
                .then(blob => {
                    let self = this
                    this.audio = new Howl({
                        src: URL.createObjectURL(blob),
                        format: ['mp3', 'aac'],
                        html5: true, 
                        onend: function() {
                            // console.log('Finished!');
                            self.isPlaying = false,
                            self.value = 0
                        }
                    });
                    this.play()
                })
            }
        },
        play() {
            if (this.audio) {
                this.isPlaying = true
                this.audio.play()
                this.updateValue() 
            }
        },
        pause() {
            if (this.audio) {
                this.isPlaying = false
                this.audio.pause()
            }
        },
        updateValue() {
            if (this.audio && this.audio.playing) {
                this.value = 100 * this.audio.seek() / this.audio.duration()
                setTimeout(() => {
                    this.updateValue()
                }, 500);
            }
        }
    },
    mounted() {
        this.$root.$on('play', (feed) => {
            this.song_url = feed.song_url
            this.song_title = feed.song_title
            this.artist_name = feed.artist_name
            if (this.audio) {
                this.audio.stop()
                this.audio.unload()
                this.audio = null
            }

            this.begin()
        })
    }
}
</script>
