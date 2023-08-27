<template>
    <div class="todo-list">
      <h1>Todo List</h1>
      <form  @submit.prevent="addTodo()">
      <!-- Añadir modelo v. -->
      <el-input  placeholder="Indique una tarea" v-model="todo" clearable></el-input>
    </form>
    <div class="clearfix">
    <el-row :gutter="12">
    <el-col v-for="(todo, index) in todos" :key="index" :span="12">
        <el-card shadow="hover" class="box-card" >
          {{ todo }}
          <el-button type="success" icon="el-icon-check" @click="showTask(index)" circle></el-button>
        </el-card>
        </el-col>
    </el-row>
  </div>
    </div>

  </template>
  <script>
  export default {
    name: 'TodoList',
     // Añadir propiedad de datos
    data() {
    return {
      todo: '',
      todos: [],
        }
    
    },
    methods: {
        addTodo(){
            this.todos.push(this.todo);
            this.todo = ''
        },
        showTask(index){
            this.todos.splice(index, 1)
        }
    }
}
  </script>