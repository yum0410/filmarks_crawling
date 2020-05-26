// https://jp.vuejs.org/v2/examples/todomvc.html
new Vue({
    el: '#app',
    data: {
        items: [
          {
            title: 'ライフ・イズ・ビューティフル',
            rate: '4.2',
            release_date: '1999年04月17日',
            show_time: '117分',
            country: 'イタリア',
            genre: ['ドラマ', '恋愛'],
            how_to_see: ['レンタル'],
            directer: 'ロベルト・ベニーニ',
            writer: 'ヴィンセンツォ・セラミ',
            actor: 'ロベルト・ベニーニニコレッタ・ブラスキ'
          },
          {
            title: 'b',
            rate: 'b',
            release_date: 'b',
            show_time: 'b',
            country: 'b',
            genre: 'b',
            how_to_see: 'b',
            directer: 'b',
            writer: 'b',
            actor: `b`
          },
          {
            title: 'c',
            rate: 'c',
            release_date: 'c',
            show_time: 'c',
            country: 'c',
            genre: 'c',
            how_to_see: 'c',
            directer: 'c',
            writer: 'c',
            actor: `c`
          }
        ],
    },
    methods: {
        // TODO
        // doCrawling: function(event) {
        //     pass
        // }

        // TODO
        // doLoadMovies: function(event) {
        //     pass
        // }
    }
})