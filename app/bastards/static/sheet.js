const Sheet = fetch('/bastards/template.html').then((response) => response.text()).then((body) => {
  return {
    template: body,
    computed: {
      character_id() {
        return this.$route.params.character_id;
      },
    },
    created() {
      this.getCharacter();
    },
    methods: {
      getCharacter() {
        this.client.then(
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
        router.push({ path: '/bastards/'}).then(() => {
          this.getCharacter();
        });
      },
      createCommoner() {
        router.push({ path: '/bastards/', query: {commoner: true}}).then(() => {
          this.getCharacter();
        });
      },
      createWithExtraClasses() {
        router.push({ path: '/bastards/', query: {extra_classes: true}}).then(() => {
          this.getCharacter();
        });
      },
    },
    data() {
      return {
        character: null,
        client: new SwaggerClient('/openapi.json'),
      };
    },
  };
});

