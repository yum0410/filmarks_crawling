var vm = new Vue({
    el: '#app',
    data: {
      items: []
    },
    created() {
      var vm = this
      var req = new XMLHttpRequest();
      req.open("get", "../results/movies_info.tsv", true);
      req.send(null);
      req.onload = function(){
        var data = req.responseText;
        const resultArray = vm.convertCsvToArray(data); 
        vm.items = resultArray
        let movies_info = []
        for (let row in resultArray) {
          movies_info.push(
            {
              title: row["title"],
              rate: row["rate"],
              release_date: row["release_date"],
              show_time: row["show_time"],
              country: row["country"],
              genre: row["genre"],
              how_to_see: row["how_to_see"],
              directer: row["directer"],
              actor: row["actor"]
            }
          )
        }
      }
    },
    methods: {
      convertCsvToArray: function(csv) {
        //header:CSV1行目の項目 :csvRows:項目に対する値
        const [header, ...csvRows] = csv.split('\n').filter(function (row) {
          if (row !== '') {
            return row;
          }
        }).map(function (row) {
          return row.split('\t');
        });

        let arrayInKeyAndValue;
        let resultArray;
        let tmpResultArray;
    
        tmpResultArray = csvRows.map(function (r) {
          arrayInKeyAndValue = header.map(function (_, index) {
            return ({key: header[index].replace(/\s+/g, ''), value: r[index]});
          });
          arrayInKeyAndValue = arrayInKeyAndValue.reduce(function (previous, current) {
            previous[current.key] = current.value;
            return previous;
          }, {});
          return arrayInKeyAndValue;
        });
    
        resultArray = tmpResultArray.reduce(function (previous, current, index) {
          previous[index] = current;
          return previous;
        }, {});
        return resultArray;
      },
      // TODO
      doCrawling: function(event) {
          alert(this.items)
      }
    }
})