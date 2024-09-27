import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StudentService {

  private url = 'http://127.0.0.1:8000/students/';

  constructor(public http: HttpClient) { }

  createStudent(student: any ){
    return this.http.post(this.url, student);
  }

  getStudents(){
    return this.http.get(this.url);
  }

  filterStudents(search: string){
    return this.http.get(this.url + '?search=' + search);
  }

}
