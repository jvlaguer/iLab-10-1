# MedVisor Frontend

This repository contains the files for the frontend code for MedVisor.

---

## Prerequisites:

- Node Version 20.15.1

## Running Locally:

To run this project locally, install the needed node modules by entering the
following command:

```shell
npm install
```

To launch the development server, enter the first command to launch the
production server launch the last two commands.

```shell
# runs the dev server
npm run dev

# builds the prod files then runs prod server
npm run build
npm run preview
```

## Tech Stack:

- Uses React with Vite as a bundler
- Styling is done using css with module files to scope styles to specific
  components
- Page Routing is done using [wouter](https://github.com/molefrog/wouter)
  - Please see Router.jsx found in `/src/Router.jsx` to change routing as
    desired
- Used icons from [Lucide Icons](https://lucide.dev/icons/)

## Conventions

- Page components in `/src/pages/`
  - Components that are only used for a specific page can be put here as well
- Components are found in `/src/components/`
  - ui components are reusable components that are either functional or used for
    layouts
  - non-ui components are reusable components that is used for design
- Images are found in `/srcs/assets/`

## Notes

- `index.html` is where the site lives, please update metadata like title and
  others here
- The react root is the div inside of the body with the id of root
