<template>
    <div>
      <h1>Lista de problemas</h1>
      <el-button  @click="getIssues()" type="success">Obtener problema</el-button>
      <el-row :gutter="12">
        <el-col v-for="(issue, index) in issues" :key="index" :span="12">
          <el-card shadow="hover" class="box-card" >
          {{ issue.title}}
          <el-button @click="closeIssue(issue.number)" type="success" icon="el-icon-check" circle></el-button>
          </el-card>
        </el-col>
    </el-row>
    </div>
  </template>
  
  <script>
  import axios from 'axios'; 
  const client = axios.create({  //--1
  baseURL: `${process.env.VUE_APP_GITHUB_ENDPOINT}`, //--2
  //baseURL: 'https://api.github.com/repos/diveintocode-corp/vue_seriese_api',
  headers: { //--3
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type':'application/json',
    'Authorization': `${process.env.VUE_APP_GITHUB_TOKEN}`
  },
})

  export default {
    name: 'IssueList',
    data(){
      return {
        issues: [],
      }
    },
    methods: {
      getIssues(){
  client.get('/issues')
    .then((res) => {
      this.issues = res.data;
    })
    .catch((error) => {
      console.error('Error fetching issues:', error);
    })
  }, 
  closeIssue(number){
      client.patch(`/issues/${number}`,
          {
            state: 'closed'
          },
        )
        .then(() => {
          this.issues.some((v, i) => {
            if(v.number == number) this.issues.splice(i, 1); 
          })
      })
    },
    created() {
    console.log('created!')
    console.log(`${process.env.VUE_APP_GITHUB_TOKEN}`)
  },
}
}

  </script>