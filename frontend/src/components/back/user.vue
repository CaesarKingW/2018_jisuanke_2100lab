<template>
  <section>
    <div class="front">
      <form>
        用户id：
        <input type="text" name="course_name">
        <button type="button">搜索</button>
      </form>
    </div>
    <div class="front">
      <Page :total="100" />
    </div>
  </section>
</template>

<script>

export default {
  name: 'user',
  data() {
    return {
      course: [],
      block: 5
    }
  }
}
</script>

<style scoped>
.front {
  position: static;
  padding-top: 50px;
  padding-bottom: 400px;
  padding-left: 400px;
  font-size: 20px;
}

</style>
