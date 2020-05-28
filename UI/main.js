var vm = new Vue({
    el: '#app',
    data: {
      items: []
    },

    created() {
      // TODO csvからの読み込みだとカンマずれおきる,SQLでの対応に変更
      var vm = this
      var req = new XMLHttpRequest();
      req.open("get", "../results/movies_info.csv", true);
      req.send(null);
      req.onload = function(){
        var data = req.responseText;
        let lines = data.split('\n');
        lines.shift();
        let lines_array = [];
        for (let i=0; i < lines.length; i++) {
          lines_array[i] = lines[i].split(",");
        }
        let movies_info = []
        for (let i=0; i < lines_array.length; i++){
          movies_info.push(
            {
              title: lines_array[i][10],
              rate: lines_array[i][7],
              release_date: lines_array[i][8],
              show_time: lines_array[i][9],
              country: lines_array[i][3],
              genre: lines_array[i][5],
              how_to_see: lines_array[i][6],
              directer: lines_array[i][4],
              actor: lines_array[i][1]
            }
          )  
        }
        vm.items = movies_info
      }
    },

    methods: {
        // TODO
        doCrawling: function(event) {
            alert(this.items)
        }
    }
})