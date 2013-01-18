/**
 *
 * @file /js/
 * @fileoverview A View
 * @author Keith DiMatteo
 * @copyright Copyright 2012, Sapient Corporation. All rights reserved.
 */

define(["txt!template/main.html"], function(tplMain){

	var BASE_URL = "http://127.0.0.1:5000";

	var URLModel = Backbone.Model.Extend({
		term : "",
		url : function(){
			return BASE_URL + "/getURL?q=" +  this.term;
		} 
	});

	var mainView = Backbone.View.extend({
		
		events: {
			"click #btnTerm" : "getTerm",
			"click #btnURL"  :  "getURL"
		},

		getTerm: function(){
			var q = $("#term").val();
		},

		getURL: function(){
			var q = $("#url").val();
		},

		initialize: function(){
			//this.collection.bind("reset", this.render, this);
		},

		render: function(){
			$("#main").html(tplMain);
			return this;
		}

	});	
});
