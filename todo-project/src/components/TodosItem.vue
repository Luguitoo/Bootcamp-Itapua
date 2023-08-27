<template>
  <div>
    <el-col :span="12">
      <el-card class="box-card" shadow="hover" style="margin: 5px 0;">
        <el-row :gutter="12">
          <el-col :span="21">{{ item.title }}</el-col>
          <el-col :span="3">
            <el-button @click="handleClick" type="success" icon="el-icon-check" circle></el-button>
          </el-col>
        </el-row>
      </el-card>
    </el-col>
  </div>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    item: Object,
    type: String,
  },
  methods: {
    handleClick() {
      if (this.type === 'todo') {
        this.$emit('remove-item'); // Emitir evento para eliminar tarea
      } else if (this.type === 'issue') {
        this.$emit('remove-item'); // Emitir evento para cerrar problema en GitHub
      }
    },
  },
};
</script>
