<template>
<div>
  <div id='addCourse'><router-link to="addCourse" tag="button" id='addCourseButton'>添加课程</router-link></div>
  <div id='editCourse'>
    <div>
      <input v-model="course_name" placeholder="请输入课程名以搜索你要编辑的课程">
      <button @click='search()'>搜索</button>
    </div>
    <div v-show='is_show'>
      <router-link :to="{path:'editCourse',params: {course_id:1}}">
        <img src='http://192.168.55.33:8000/media/user_photos/a4dbd2628535e5ddc122f8007fc6a7efcf1b62f8.jpg' width=50px height=60px>
      </router-link>
    </div>
  </div>
</div>
</template>
<script>
export default {
  name: 'course',
  data() {
    return {
      is_show: true,
      course_name: '',
      courses: []
    }
  }
}
</script>
<style>
#addCourse {
  background-color:violet;
  }
#addCourseButton {
  background-color: skyblue;
  color: white;
}
</style>
