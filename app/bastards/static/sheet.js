const Sheet = fetch('/bastards/template.html').then((response) => response.text()).then((body) => {
  return {
    template: body,
    computed: {
      character_id() {
        return this.$route.params.character_id;
      },
    },
    created() {
      new SwaggerClient('/openapi.json').then(
        (client) => {
          if (this.$route.params.character_id) {
            client.apis.bastards.get_character({character_id: this.$route.params.character_id}).then((resp) => {
              this.character = resp.body;
            });
          } else {
            client.apis.bastards.get_new_character().then((resp) => {
              this.character = resp.body;
            });
          };
        },
      );
    },
    methods: {
      getLoad() {
        let current_load = 0;
        for (i=0; i<this.character.inventory.length; i++) {
          current_load += this.character.inventory[i].slots;
        };
        return `${current_load}/${this.character.max_load}`;
      },
      getWeaponData(item){
        let note = item.size;
        if (item.throwable) {
          note += ", throwable";
        };
        if (item.twohanded) {
          note += ", two-handed";
        };
        if (item.ranged) {
          note += ", ranged";
        };
        return `${note}`;
      },
      copyLink() {
        navigator.clipboard.writeText(`${window.location.origin}/bastards/${this.character.seed}${window.location.search}`);
      },
      createCharacter() {
        router.go({ path: '/bastards/'})
      },
      createCommoner() {
        router.go({ path: '/bastards/', query: {commoner: true}})
      },
      createWithExtraClasses() {
        router.go({ path: '/bastards/', query: {extra_classes: true}})
      },
    },
    data() {
      return {
        character: null,
      };
    },
  };
});

