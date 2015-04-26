//
//  ViewController.swift
//  ImperiiViz
//
//  Created by Frederik Riedel on 26.04.15.
//  Copyright (c) 2015 Frederik Riedel. All rights reserved.
//

import UIKit

class ViewController: UIViewController,UITextFieldDelegate,TimeLineViewDelegate {

    var dateIndicator : DateIndicator?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.view.backgroundColor=UIColor.whiteColor()
        
        //var backgroundImage = UIImageView(frame: CGRectMake(0, 0, self.view.frame.width, self.view.frame.height))
        //backgroundImage.image=UIImage(named: "Startpage")
        //self.view.addSubview(backgroundImage)
        
        /*var suchfled = UITextField(frame: CGRectMake((self.view.frame.width-400)/2, (self.view.frame.height-44)/2, 400, 44))
        suchfled.backgroundColor=UIColor.darkGrayColor()
        self.view.addSubview(suchfled)*/
        
        NSNotificationCenter.defaultCenter().addObserver(self, selector:"keyboardWillChange:", name:UIKeyboardWillChangeFrameNotification, object:nil)
        
        
        var from = NSDateComponents()
        from.year = 1101
        
        var to = NSDateComponents()
        to.year = 2015
        
        
        
        var timeLineView = TimeLineView(frame: CGRectMake(0, self.view.frame.height-55, self.view.frame.size.width, 55), from: from, to: to)
        timeLineView.delegate=self
        self.view.addSubview(timeLineView)
        
        dateIndicator = DateIndicator(frame: CGRectMake(100, self.view.frame.height-110, 100, 55))
        self.view.addSubview(dateIndicator!)
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    func yearChanged(year: Float) {
        dateIndicator?.setYear(year)
    }
        
    


}

