// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint256 studentId;
        string name;
        uint256 age;
    }

    Student[] public students;

    event StudentAdded(uint256 studentId, string name, uint256 age);
    event StudentUpdated(uint256 studentId, string name, uint256 age);

    function addStudent(uint256 _studentId, string memory _name, uint256 _age) public {
        Student memory newStudent = Student(_studentId, _name, _age);
        students.push(newStudent);
        emit StudentAdded(_studentId, _name, _age);
    }

    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        require(index < students.length, "Student not found");
        Student memory student = students[index];
        return (student.studentId, student.name, student.age);
    }

    function updateStudent(uint256 index, string memory _name, uint256 _age) public {
        require(index < students.length, "Student not found");
        students[index].name = _name;
        students[index].age = _age;
        emit StudentUpdated(students[index].studentId, _name, _age);
    }

    // Fallback function to accept Ether (optional)
    receive() external payable {}

    // Fallback function for receiving Ether without data (optional)
    fallback() external payable {}
}
