// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'M7-Engenharia-Computação',
  tagline: 'Engenharia de Computação',
  favicon: 'img/inteli.svg',

  // Set the production url of your site here
  url: 'https://murilo-zc.github.io/',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/M7-Inteli-Eng-Comp/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Inteli', // Usually your GitHub org/user name.
  projectName: 'M7-Eng-Comp', // Usually your repo name.

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'pt-br',
    locales: ['pt-br'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          routeBasePath: '/',
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/m10-social-card.jpg',
      navbar: {
        title: 'M7 - Sistema de manutenção preditiva com IA e arquitetura em nuvem',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo-eng-comp.png',
        },
        items: [
          {
            href: 'https://github.com/Murilo-ZC/M7-Inteli-Eng-Comp',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Links',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Murilo-ZC/M7-Inteli-Eng-Comp',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Murilo-Tech, made with ♥️, ☕️ and 🐞 (sorry, but it's true). Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['dart', 'protobuf'],
      },
    }),
};

export default config;
