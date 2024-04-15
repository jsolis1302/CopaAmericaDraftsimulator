import { Component, Input, OnInit } from '@angular/core';
import { Country } from 'src/assets/shared/country.model';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-select-country',
  templateUrl: './select-country.component.html',
  styleUrls: ['./select-country.component.css']
})
export class SelectCountryComponent implements OnInit{

  GA:Country[] = [];
  GB:Country[] = [];
  GC:Country[] = [];
  GD:Country[] = [];

  @Input() QFin:Country[] = [];
  selectedClass:any = 0;

  constructor(private service:SharedService){}


  ngOnInit(): void {
    this.service.getFirstGroup().subscribe(data=>{
      this.GA= data;
      
    });

    this.service.getSecondGroup().subscribe(data=>{
      this.GB= data;
      
    });

    this.service.getThirdGroup().subscribe(data=>{
      this.GC= data;
      
    });

    this.service.getLastGroup().subscribe(data=>{
      this.GD= data;
      
    });

    
  }

  clickedQF(item:Country,idx:any) {
    console.log("rowclcicked "+this.selectedClass);
    console.log("idx "+idx);
    
    if (this.selectedClass === idx) {
      this.selectedClass = -1;
    }
    else {
      this.selectedClass = idx;
    }
    this.QFin.push(item);
   
  }

  isSelectedComp(gName:string){
    if (gName === 'A'){
      return this.QFin.length < 2;
    }
    else if (gName === 'B'){
      
      return this.QFin.length >= 2 && this.QFin.length < 4;
    }
    else if (gName === 'C'){
      return this.QFin.length >= 4 && this.QFin.length < 6;
    }
    else if (gName === 'D'){
      return this.QFin.length >= 6 && this.QFin.length < 8;
    }
    else {
      
      return false;
    }
    


}


}








