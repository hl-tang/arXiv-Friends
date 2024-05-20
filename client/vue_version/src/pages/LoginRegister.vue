<template>
  <div class="min-h-screen flex items-center justify-center ">
    <div class="w-full max-w-md">
      <div class="bg-white p-8 rounded-lg shadow-lg">
        <div class="mb-4">
          <div class="flex justify-around">
            <button :class="{ 'text-red-500 border-b-2 border-red-500': isLogin, 'text-gray-500': !isLogin }"
              @click="isLogin = true" class="py-2 px-4 focus:outline-none">
              Login
            </button>
            <button :class="{ 'text-red-500 border-b-2 border-red-500': !isLogin, 'text-gray-500': isLogin }"
              @click="isLogin = false" class="py-2 px-4 focus:outline-none">
              Register
            </button>
          </div>
        </div>
        <div v-if="isLogin">
          <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Login</h2>
          <form @submit.prevent="handleLogin">
            <!-- <div class="mb-4">
              <label class="block text-gray-700 text-sm font-bold mb-2" for="loginEmail">Email</label>
              <input v-model="loginEmail" id="loginEmail" type="email" placeholder="Email"
                class="w-full px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:ring focus:border-red-500" />
            </div> -->
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-bold mb-2" for="loginUsername">Username</label>
              <input v-model="loginUsername" id="username" type="text" placeholder="Username"
                class="w-full px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:ring focus:ring-red-200" />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-bold mb-2" for="loginPassword">Password</label>
              <input v-model="loginPassword" id="loginPassword" type="password" placeholder="Password"
                class="w-full px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:ring focus:ring-red-200" />
            </div>
            <div class="flex items-center justify-between">
              <button type="submit"
                class="w-full bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring focus:border-red-500">
                Login
              </button>
            </div>
          </form>
        </div>
        <div v-else>
          <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">Register</h2>
          <form @submit.prevent="handleRegister">
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-bold mb-2" for="registerUsername">Username</label>
              <input v-model="registerUsername" id="registerUsername" type="text" placeholder="Username"
                class="w-full px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:ring focus:ring-red-200" />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-bold mb-2" for="registerPassword">Password</label>
              <input v-model="registerPassword" id="registerPassword" type="password" placeholder="Password"
                class="w-full px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:ring focus:ring-red-200" />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-bold mb-2" for="confirmPassword">Confirm Password</label>
              <input v-model="confirmPassword" id="confirmPassword" type="password" placeholder="Confirm Password"
                class="w-full px-3 py-2 border rounded-lg text-gray-700 focus:outline-none focus:ring focus:ring-red-200" />
            </div>
            <div class="flex items-center justify-between">
              <button type="submit"
                class="w-full bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring focus:border-red-500">
                Register
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const isLogin = ref(true);
const loginUsername = ref('');
const loginPassword = ref('');
const registerUsername = ref('');
const registerPassword = ref('');
const confirmPassword = ref('');

const res_data = ref({});
import { useRoute, useRouter } from "vue-router"
const route = useRoute()
const router = useRouter()

import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { isLoggedIn } = storeToRefs(useIsLoggedInStore())


const handleLogin = async () => {
  // Handle login logic here
  console.log('登录中...');
  console.log('用户名:', username.value);
  try {
    await axios.post("/api/login/", {
    // await axios.post("http://localhost:8000/api/login/", {
      username: loginUsername.value,
      password: loginPassword.value
    }).then(res => {
      isLoggedIn.value = true;
      console.log("Response Data:", res.data);
      // res_data = res.data  一定注意.value
      res_data.value = res.data
      console.log(res_data.value.msg)
      alert(res_data.value.msg)
      if (res_data.value.msg === "Login successful") {
        // 等待2秒后执行跳转页面的操作
        setTimeout(() => {
          router.push("/");
        }, 2000);
      }
    });
  } catch (error) {
    console.error(error.response.data.message);
  }
};

const handleRegister = async () => {
  // Handle register logic here
  if (registerPassword.value !== confirmPassword.value) {
    alert('Passwords do not match');
    return;
  }
  try {
    await axios.post("/api/register/", {
      username: registerUsername.value,
      password: registerPassword.value,
    }).then(res => {
      console.log("Response Data:", res.data);
      // res_data = res.data  一定注意.value
      res_data.value = res.data
      alert(res_data.value.msg)
      if (res_data.value.msg === "User created successfully") {
        setTimeout(() => {
          isLogin.value = true;
        }, 1000);
      }
    });
  } catch (error) {
    console.error(error.response.data.message);
  }
};

console.log("isLoggedIn 1", isLoggedIn.value);
</script>

<style scoped>
/* Add any additional styles here */
</style>
