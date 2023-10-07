import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// import Icons from 'unplugin-icons/vite'
// import IconsResolver from 'unplugin-icons/resolver'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
// import Inspect from 'vite-plugin-inspect'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  server: { //https://cn.vitejs.dev/config/server-options.html
  	open: false,	//npm run dev后不要自动打开浏览器，不然docker log查了就知道有报错Error: spawn xdg-open ENOENT
  	port: 5173,	//不配ip的话，docker run -p是跑不起来的
  	host: '0.0.0.0'
  },
})
