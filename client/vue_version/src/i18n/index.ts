// https://vue-i18n.intlify.dev/guide/installation.html
import { createI18n } from 'vue-i18n'
import localEn from './languages/en.ts'
import localJa from './languages/ja.ts'
import localZhCn from './languages/zh-cn.ts'

const i18n = createI18n({
    legacy: false,
    locale: 'ja',
    messages: {
        'en': localEn,
        'ja': localJa,
        'zh-cn': localZhCn
    }
})

export default i18n