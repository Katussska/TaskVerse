/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    darkMode: 'selector',
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'

        'node_modules/preline/dist/*.js',
    ],
    theme: {

        fontFamily: {
            title: ['Assistant', 'sans-serif'],
            paragraph: ['Work Sans', 'sans-serif'],
            complementary: ['Hind Madurai', 'sans-serif'],
        },
        extend: {
            textColor: {
                DEFAULT: 'var(--text-color)'
            },
            colors: {
                primary: {
                    '50': 'var(--primary-50)',
                    '100': 'var(--primary-100)',
                    '200': 'var(--primary-200)',
                    '300': 'var(--primary-300)',
                    '400': 'var(--primary-400)',
                    DEFAULT: 'var(--primary)',
                    '600': 'var(--primary-600)',
                    '700': 'var(--primary-700)',
                    '800': 'var(--primary-800)',
                    '900': 'var(--primary-900)',
                    '950': 'var(--primary-950)',
                },
                secondary: {
                    '50': 'var(--secondary-50)',
                    '100': 'var(--secondary-100)',
                    '200': 'var(--secondary-200)',
                    '300': 'var(--secondary-300)',
                    '400': 'var(--secondary-400)',
                    DEFAULT: 'var(--secondary)',
                    '600': 'var(--secondary-600)',
                    '700': 'var(--secondary-700)',
                    '800': 'var(--secondary-800)',
                    '900': 'var(--secondary-900)',
                    '950': 'var(--secondary-950)',
                },
                accent: {
                    '50': 'var(--accent-50)',
                    '100': 'var(--accent-100)',
                    '200': 'var(--accent-200)',
                    '300': 'var(--accent-300)',
                    '400': 'var(--accent-400)',
                    DEFAULT: 'var(--accent)',
                    '600': 'var(--accent-600)',
                    '700': 'var(--accent-700)',
                    '800': 'var(--accent-800)',
                    '900': 'var(--accent-900)',
                    '950': 'var(--accent-950)',
                },
                background: 'var(--background)',
                'background-alt': 'var(--background-alt)',
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require('preline/plugin'),
    ],
}
