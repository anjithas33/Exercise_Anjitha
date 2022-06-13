<template>
  <DockMenu :items="items" :theme="{
    primary: '#b2b2b2',
    secondary: '#e5e5e5',
    textHoverColor: '#9BA3EB'
  }" />
</template>
<script>
import { DockMenu } from "vue-dock-menu";
import "vue-dock-menu/dist/vue-dock-menu.css";

export default {
  name: "App",
  components: {
    DockMenu,
  },

  data() {
    return {
      items: [
        {
          name: "About Tecnopark",

          menu: [
            { name: "Thiruvanathapuram" },
            { isDivider: true },
            { name: "Tenders" },
            { isDivider: true },
            { name: "Governing Body" },
            { isDivider: true },
            {
              name: "Executive Council",
              menu: [
                { name: "Inernational complaince committe" },
                { name: "Right to work" },
              ],
            },
          ],
        },
        {
          name: "Life of Technopark",
          menu: [
            { name: "News" },
            { isDivider: true },
            { name: "Gallery" },
            { isDivider: true },
            { name: "Help desk" },
          ],
        },
        {
          name: "Infrastructure",

          menu: [
            { name: "Why Technopark" },
            { isDivider: true },
            {
              name: "Phasewise Details",
              menu: [{ name: "Phase1" },
              { isDivider: true },
              { name: "Phase2" },
              { isDivider: true },
              { name: "Phase3" }],
            },
          ],
        },
      ],
    };
  },
};
</script>


