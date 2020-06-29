<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center color="primary">
            <v-flex xs12 sm8 md4 color="primary">
                <v-card>
                    <v-card-title primary-title>
                        <h1 class="text-lg-center">Sign Up Form</h1>
                    </v-card-title>

                    <v-card-text>
                        <v-form 
                            ref="form"
                            @submit.prevent
                        >
                            <v-text-field 
                                v-model="username"
                                :rules="nameRules" 
                                label="User name" 
                                type="text"
                                required
                            ></v-text-field>
                            <v-text-field 
                                v-model="firstname"
                                :rules="nameRules" 
                                label="First name" 
                                type="text"
                                required
                            ></v-text-field>
                            <v-text-field 
                                v-model="lastname"
                                :rules="nameRules" 
                                label="Last name" 
                                type="text"
                                required
                            ></v-text-field>
                            <v-text-field 
                                v-model="email"
                                :rules="emailRules" 
                                label="E-mail" 
                                type="text"
                                required
                            ></v-text-field>
                            <v-menu
                                v-model="menu"
                                :close-on-content-click="false"
                                :nudge-right="40"
                                lazy
                                transition="scale-transition"
                                offset-y
                                full-width
                                min-width="290px"
                            >
                                <template v-slot:activator="{ on }">
                                    <v-text-field
                                        v-model="birthdate"
                                        :rules="birthDateRule" 
                                        label="Birthdate"
                                        readonly
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker v-model="birthdate" @input="menu = false"></v-date-picker>
                            </v-menu>
                            <v-autocomplete 
                                v-model="gender"
                                :rules="[() => !!gender || 'Gender is required']"
                                :items="genders"
                                label="Gender"
                                placeholder="Select..."
                                required
                            ></v-autocomplete>
                            <v-autocomplete
                                v-model="country"
                                :rules="[() => !!country || 'Country is required']"
                                :items="countries"
                                label="Country"
                                placeholder="Select..."
                                required
                            ></v-autocomplete>
                            <v-text-field 
                                :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                                v-model="password" 
                                :rules="passwordRule" 
                                label="Password" 
                                :type="showPassword ? 'text' : 'password'"
                                @click:append="showPassword = !showPassword"
                                required
                            ></v-text-field>
                            <v-text-field 
                                :append-icon="showConfirmedPassword ? 'visibility' : 'visibility_off'"
                                v-model="confirmedPassword" 
                                :rules="[passwordConfirmationRule]" 
                                label="Confirm Password" 
                                :type="showConfirmedPassword ? 'text' : 'password'"
                                @click:append="showConfirmedPassword = !showConfirmedPassword"
                                required
                            ></v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn :color="color" @click="submit">Submit</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import Service from '@/service';
const service = new Service();

  export default {
    data: () => ({
        username: '',
        firstname: '',
        lastname: '',
        nameRules: [
            v => !!v || 'Name is required',
            v => v.length <= 20 || 'Name must be less than 20 characters'
        ],
        email: '',
        emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+/.test(v) || 'E-mail must be valid'
        ],
        birthdate: null,
        birthDateRule: [
            v => !!v || 'Date of birth is required',
        ],
        menu: false,
        gender: '',
        genders: [
            'Male', 
            'Female'
        ],
        country: '',
        countries: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua &amp; Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia &amp; Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote D Ivoire', 'Croatia', 'Cruise Ship', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'French West Indies', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Pierre &amp; Miquelon', 'Samoa', 'San Marino', 'Satellite', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'St Kitts &amp; Nevis', 'St Lucia', 'St Vincent', 'St. Lucia', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', "Timor L'Este", 'Togo', 'Tonga', 'Trinidad &amp; Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks &amp; Caicos', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Virgin Islands (US)', 'Yemen', 'Zambia', 'Zimbabwe'],
        showPassword: false,
        password: '',
        passwordRule: [
            v => !!v || 'Password is required'
        ],
        showConfirmedPassword: false,
        confirmedPassword: '',
        color: "green",
    }),
    methods: {
        submit() {
            if (this.$refs.form.validate()) {
                // console.log(this.username, this.password)
                service.createUser({
                    "username": this.username,
                    "email": this.email,
                    "password": this.password,
                    "detail": {
                        "firstname": this.firstname,
                        "lastname": this.lastname,
                        "gender": this.gender,
                        "birthdate": this.birthdate,
                        "country": this.country
                    }
                }).then(()=>{
                    alert("Customer created!");
                }).catch(()=>{
                    alert('There was an error! Please re-check your form.');
                });
                this.$refs.form.reset()
                this.username = ''
                this.firstname = ''
                this.lastname = ''

                this.$router.push('/login')
            }
        }
    },

    computed: {
        passwordConfirmationRule() {
            return () => (this.password === this.confirmedPassword) || 'Passwords don\'t match'
        }
    }
  }
</script>