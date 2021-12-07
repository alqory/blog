module.exports = {
  purge: [
    './src/**/*.html',
    './src/**/*.js',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      dropShadow: {
        '10xl': '0 35px 35px rgba(0, 0, 0, 0.25)',
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
