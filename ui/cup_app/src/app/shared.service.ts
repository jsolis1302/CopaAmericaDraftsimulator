import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from 'rxjs';
import Swal from 'sweetalert2';
import { Country } from 'src/assets/shared/country.model';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = 'http://127.0.0.1:8000'

  groupA:Country[] = [];
  groupB:Country[] = [];
  groupC:Country[] = [];
  groupD:Country[] = [];
  testGroup: Country[] = [];
 
  constructor(private http:HttpClient) { }

  getCountryList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/country/')
  }

  startDraft():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/startDraft/')
  }

  getGroup(groupName:string):Observable<Country[]>{
    return this.http.get<any[]>(this.APIUrl + '/group/'+groupName)
  }


  getFirstGroup():Observable<Country[]>{
    return this.http.get<any[]>(this.APIUrl + '/groupA/')
  }

  getSecondGroup():Observable<Country[]>{
    return this.http.get<any[]>(this.APIUrl + '/groupB/')
  }

  getThirdGroup():Observable<Country[]>{
    return this.http.get<any[]>(this.APIUrl + '/groupC/')
  }

  getLastGroup():Observable<Country[]>{
    return this.http.get<any[]>(this.APIUrl + '/groupD/')
  }

  resetDraft(){
    return this.http.delete(this.APIUrl + '/resetDraft/')
  }

  startKOPhase(){
    return this.http.get<any[]>(this.APIUrl + '/kophase/')
  }

  getGA(){
    this.getFirstGroup().subscribe(data=>{
      this.groupA= data;
      
    });
    return this.groupA;

  }

  msgAlert = (icon:any,title:string,text:string)=>{
    Swal.fire({
      icon,
      title,
      text
    })

  }


}
