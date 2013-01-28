/**
 *
 * @file /js/
 * @fileoverview A View
 * @author Keith DiMatteo
 */

$(function(){
	"use strict";
	var BASE_URL = ""; //"http://127.0.0.1:5000";


	/**
	 * Process a Term on Twitter
	 * ----------------------------------
	 */

	var TermModel = Backbone.Model.extend({
		url : function(){
			return BASE_URL + "/term/"; //+ this.params["term"]
		}
	});

	var TermView = Backbone.View.extend({
		el : $("#main"),
		events: {
			"click #btnTerm" : "getTerm"
		},
		initialize: function(){
			this.model.bind("change", this.render, this);
		},
		getTerm: function(){
			var q = $("#term").val();
			this.model.fetch({data:{"term":q}});
			$("#termIndicator").removeClass("hidden");
			$("#termIndicator").show();
		},
		render: function(){
			var responseObj = this.model.toJSON();
			$("#termIndicator").hide();
			$("#termResults").empty();
			
			for(var index in responseObj.calais_results.entities){
				if (responseObj.calais_results.entities.hasOwnProperty(index)){
					$("#termResults").append("<li>" + responseObj.calais_results.entities[index]);
				}
			}
		}

	});
	
	var termView = new TermView({model:new TermModel()});


	/**
	 * Process a URL
	 * ----------------------------------
	 */

	var URLModel = Backbone.Model.extend({
		url : function(){
			return BASE_URL + "/url/"; //+ this.params["term"]
		}
	});

	var URLView = Backbone.View.extend({
		el : $("#main"),
		events: {
			"click #btnURL" : "getTerm"
		},
		initialize: function(){
			this.model.bind("change", this.render, this);
		},
		getTerm: function(){
			var q = $("#url").val();
			this.model.fetch({data:{"term":q}});
			$("#urlIndicator").removeClass("hidden");
			$("#urlIndicator").show();
		},
		render: function(){
			var responseObj = this.model.toJSON();
			$("#urlIndicator").hide();
			$("#urlResults").empty();
			for(var key in responseObj.response){
				if (responseObj.response.hasOwnProperty(key)){
					$("#urlResults").append("<li>" + responseObj.response[key]["categoryName"]);
				}
			}
		}
	});

	var urlView = new URLView({model:new URLModel()});

});