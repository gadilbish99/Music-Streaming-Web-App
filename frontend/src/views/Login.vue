<template>
    <v-container fluid fill-height @keyup.enter="submit">
        <v-layout align-center justify-center color="primary">
            <v-flex xs12 sm8 md4 color="primary">
                <v-card>
                    <v-card-title primary-title>
                        <h1 class="text-lg-center">Login Form</h1>
                    </v-card-title>

                    <v-card-text>
                        <v-form 
                            ref="form"
                        >
                            <v-text-field 
                                prepend-icon="email" 
                                v-model="email"
                                :rules="emailRules" 
                                label="Email Address" 
                                type="text"
                                required
                            ></v-text-field>
                            <v-text-field 
                                prepend-icon="lock" 
                                v-model="password" 
                                :rules="passwordRule" 
                                label="Password" 
                                type="password"
                                required
                            ></v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn :color="color" @click="submit">Login</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
  export default {
    data: () => ({
        email: '',
        emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+/.test(v) || 'E-mail must be valid'
        ],
        password: '',
        passwordRule: [
            v => !!v || 'Password is required'
        ],
        color: "green",
    }),
    methods: {
        submit() {
            if (this.$refs.form.validate()) {
                this.$store.dispatch('login', {
                    'email': this.email,
                    'password': this.password,
                })
                .then(() => this.$router.push('/'))
                .catch(err => alert(err))
                   
                this.$refs.form.reset()
            }
        }
    }
  }
</script>

