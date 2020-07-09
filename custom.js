(function()
{
	var app=angular.module('myapp',[]);
	app.controller("myController",["$scope",myController]);
	var excelJsonObj=[];
	function myController($scope,$http){

		$scope.uploadExcel=function()
		{
			$scope.Clicked=true;
			var myFile=document.getElementById('file');
			var input=myFile;
			var reader=new FileReader();
			reader.onload=function()
			{
				var fileData=reader.result;
				var workbook=XLSX.read(fileData,{type:'binary'});
				workbook.SheetNames.forEach(function(sheetName)
				{
var rowObject=XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheetName]);
excelJsonObj=rowObject;
				});
		for (var i = 0; i <excelJsonObj.length; i++) {
			var data=excelJsonObj[i];
			$('#myTable tbody:last-child').append("<tr><td>"+data.Item+"</td><td>"+data.Cost+"</td></tr>");
			}
		};
reader.readAsBinaryString(input.files[0]);


 var data = $scope.myFile;
//  var file = ... // get from file input;
// var fd = new FormData();
// fd.append('myFile', file, 'filename.ext');

    // $http.post("https://upload2017.blob.core.windows.net/test2017/myblockblob", data).then(
    //   function successCallback(response) {
    //     console.log("Successfully POST-ed data");
    //   },
    //   function errorCallback(response) {
    //     console.log("POST-ing of data failed");
    //   }
    // );



	}





}

})();