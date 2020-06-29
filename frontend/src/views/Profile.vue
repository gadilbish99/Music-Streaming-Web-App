<template>
    <v-content>
        <v-container fluid grid-list-md>
            <v-layout align-center justify-center>
              <v-card width="300">
                <table>
                  <tr>
                    <th>Username</th>
                    <th>{{info.username}} </th>
                  </tr>
                  <tr>
                    <td>Email</td>
                    <td>{{info.email}} </td>
                  </tr>
                  <tr>
                    <td>First Name</td>
                    <td>{{detail.firstname}} </td>
                  </tr>
                  <tr>
                    <td>Last Name</td>
                    <td>{{detail.lastname}} </td>
                  </tr>
                  <tr>
                    <td>Date of Birth</td>
                    <td>{{detail.birthdate}} </td>
                  </tr>
                  <tr>
                    <td>Country</td>
                    <td>{{detail.country}} </td>
                  </tr>
                  <tr>
                    <td>Gender</td>
                    <td>{{detail.gender}} </td>
                  </tr>
                  <tr>
                    <td>Joined Date</td>
                    <td>{{detail.joined_date}} </td>
                  </tr>
                </table>
            </v-card>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
import Service from '@/service';
const service = new Service();

export default {
  data () {
    return {
      info: {},
      detail: {}
    }
  },
  mounted() {
    service.getUserData()
    .then(result => {
      this.info = result[0]
      this.detail = this.info.detail
    })
  }
}
</script>

<style scoped>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

</style>