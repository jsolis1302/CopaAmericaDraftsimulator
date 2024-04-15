import { Component } from '@angular/core';
import { SharedService } from '../shared.service';
import { Country } from 'src/assets/shared/country.model';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {

  constructor(private service:SharedService){}
  ngOnInit(): void {
    this.getCountries();
  }

  CountryList:Country[] =[];

  getCountries(){
    this.service.getCountryList().subscribe(data=>{
      this.CountryList = data;
      //console.log(this.CountryList);
      this.CountryList[0] = 
        new Country(this.CountryList[0].CountryId,
          this.CountryList[0].CountryFlag,this.CountryList[0].CountryName+"*", this.CountryList[0].CountryCode,
          this.CountryList[0].CountryRank, this.CountryList[0].CountryConf
        );
        this.CountryList[1] = 
        new Country(this.CountryList[1].CountryId,
          this.CountryList[1].CountryFlag,this.CountryList[1].CountryName+"*", this.CountryList[1].CountryCode,
          this.CountryList[1].CountryRank, this.CountryList[1].CountryConf
        );

        this.CountryList[2] = 
        new Country(this.CountryList[2].CountryId,
          this.CountryList[2].CountryFlag,this.CountryList[2].CountryName+"*", this.CountryList[2].CountryCode,
          this.CountryList[2].CountryRank, this.CountryList[2].CountryConf
        );
    });
  }

}
