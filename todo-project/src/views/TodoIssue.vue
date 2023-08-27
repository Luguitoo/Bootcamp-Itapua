<template>
  <div>
    <h1>Issues</h1>
    <form @submit.prevent="addTodo()">
      <el-input placeholder="todo" v-model="todo"></el-input>
    </form>
    <el-row :gutter="12">
      <TodoItem v-for="(todo, index) in todos" :key="'todo-' + index" :item="{ title: todo }" :type="'todo'" @remove-item="removeItem(index)" />
      <TodoItem v-for="(issue, index) in issues" :key="'issue-' + issue.id" :item="issue" :type="'issue'" @remove-item="closeIssue(index)" />
    </el-row>
  </div>
</template>

<script>
import axios from 'axios';
import TodoItem from '@/components/TodosItem.vue';

const client = axios.create({
  baseURL: `${process.env.VUE_APP_GITHUB_ENDPOINT}`,
  headers: {
    'Authorization': `token ${process.env.VUE_APP_GITHUB_TOKEN}`,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
  },
})

export default {
  name: 'TodosIssues',
  components: {
    TodoItem,
  },
  data() {
    return {
      todo: '',
      todos: [],
      issues: [],
    }
  },
  methods: {
    closeIssue(index) {
      const target = this.issues[index];
      client.patch(`/issues/${target.number}`, {
        state: "closed",
      })
        .then(() => {
          this.issues.splice(index, 1);
        })
        .catch((error) => {
          console.error('Error closing issue:', error);
        });
    },
    addTodo() {
      this.todos.push(this.todo);
      this.todo = '';
    },
    getIssues() {
      client.get('issues')
        .then((res) => {
          this.issues = res.data
        })
        .catch((error) => {
          console.error('Error fetching issues:', error);
        });
    },
    removeItem(index) {
      // Remove either a todo or an issue based on index
      if (index >= 0 && index < this.todos.length) {
        this.todos.splice(index, 1);
      } else if (index >= 0 && index < this.issues.length) {
        this.issues.splice(index, 1);
      }
    },
  },
  created() {
    this.getIssues();
  },
}
</script>
