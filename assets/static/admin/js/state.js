const countryStateInfo = {
    USA: {
      California: {
        "Los Angeles": ["90001", "90002", "90003", "90004"],
        "San Diego": ["92093", "92101"],
      },
      Texas: {
        Dallas: ["75201", "75202"],
        Austin: ["73301", "73344"],
      },
    },
    Germany: {
      Bavaria: {
        Munich: ["80331", "80333", "80335", "80336"],
        Nuremberg: ["90402", "90403", "90404", "90405"],
      },
      Hessen: {
        Frankfurt: ["60306", "60308", "60309", "60310"],
        Surat: ["55246", "55247", "55248", "55249"],
      },
    },
  };



  window.onload = function () {
    //todo: Get all input html elements from the DOM
  
    const countrySelection = document.querySelector("#Country"),
      stateSelection = document.querySelector("#State"),
      citySelection = document.querySelector("#City"),
      zipSelection = document.querySelector("#Zip");


      // todo: Disable all  Selection by setting disabled to false
  stateSelection.disabled = true; // remove all options bar first
  citySelection.disabled = true; // remove all options bar first
  zipSelection.disabled = true; // remove all options bar first

  for (let country in countryStateInfo) {
    countrySelection.options[countrySelection.options.length] = new Option(
      country,
      country
    );
  }



  }