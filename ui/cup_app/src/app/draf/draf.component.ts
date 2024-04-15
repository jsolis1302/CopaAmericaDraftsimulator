import { Component } from '@angular/core';
import { GroupSort } from 'src/assets/group.model';
import { SharedService } from '../shared.service';


@Component({
  selector: 'app-draf',
  templateUrl: './draf.component.html',
  styleUrls: ['./draf.component.css']
})
export class DrafComponent {

  constructor(private service:SharedService){}
  CountryList:any =[];
  groups = [new GroupSort('A',[]),new GroupSort('B',[]),new GroupSort('C',[]),new GroupSort('D',[])];
  

  getGroupLength(){
    return this.groups[0].countries.length > 0 && this.groups[1].countries.length > 0 && this.groups[2].countries.length> 0 &&this.groups[3].countries.length >0;
  }

  startDraft(){

    this.service.startDraft().subscribe(data=>{
      this.CountryList = data;
    });

    this.service.getGroup('A').subscribe(data=>{
      this.groups[0].countries = data;
    });

    this.service.getGroup('B').subscribe(data=>{
      this.groups[1].countries = data;
    });

    this.service.getGroup('C').subscribe(data=>{
      this.groups[2].countries = data;
    });

    this.service.getGroup('D').subscribe(data=>{
      this.groups[3].countries = data;
    });

  }

  ngReset(){
    this.service.resetDraft().subscribe(data=>{
      
      this.service.msgAlert('success','Succes !!',data.toString());
      this.groups[0].countries = [];
      this.groups[1].countries = [];
      this.groups[2].countries = [];
      this.groups[3].countries = [];

    })
  }

}
