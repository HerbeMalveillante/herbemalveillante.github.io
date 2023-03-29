/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./**/*.{html,js}"],
	theme: {
		extend: {
			fontFamily: {
				bungee: ["Bungee", "cursive"],
				ubuntu: ["Ubuntu Condensed", "sans-serif"],
			},
		},
	},
	plugins: [],
};
